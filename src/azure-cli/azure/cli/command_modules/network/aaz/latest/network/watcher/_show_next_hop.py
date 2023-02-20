# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network watcher show-next-hop",
)
class ShowNextHop(AAZCommand):
    """Get information on the `next hop` of a VM.

    Requires that Network Watcher is enabled for the region in which the VM is located. For more information about show-next-hop visit https://learn.microsoft.com/en-us/azure/network-watcher/diagnose-vm-network-routing-problem-cli.

    :example: Get the next hop from a VMs assigned IP address to a destination at 10.1.0.4.
        az network watcher show-next-hop -g MyResourceGroup --vm MyVm --source-ip 10.0.0.4 --dest-ip 10.1.0.4
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkwatchers/{}/nexthop", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.watcher_name = AAZStrArg(
            options=["--watcher-name"],
            help="Name of the network watcher.",
            required=True,
            id_part="name",
        )
        _args_schema.watcher_rg = AAZResourceGroupNameArg(
            options=["--watcher-rg"],
            help="Name of the resource group the watcher is in.",
            required=True,
        )
        _args_schema.dest_ip = AAZStrArg(
            options=["--dest-ip"],
            help="Destination IPv4 address.",
            required=True,
        )
        _args_schema.source_ip = AAZStrArg(
            options=["--source-ip"],
            help="Source IPv4 address.",
            required=True,
        )
        _args_schema.nic = AAZStrArg(
            options=["--nic"],
            help="Name or ID of the NIC resource to test. If the VM has multiple NICs and IP forwarding is enabled on any of them, this parameter is required.",
        )
        _args_schema.vm = AAZStrArg(
            options=["--vm"],
            help="Name or ID of the VM to target. If the name of the VM is provided, the `--resource-group` is required.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.NetworkWatchersGetNextHop(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetworkWatchersGetNextHop(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/nextHop",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkWatcherName", self.ctx.args.watcher_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.watcher_rg,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("destinationIPAddress", AAZStrType, ".dest_ip", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("sourceIPAddress", AAZStrType, ".source_ip", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("targetNicResourceId", AAZStrType, ".nic")
            _builder.set_prop("targetResourceId", AAZStrType, ".vm", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _ShowNextHopHelper._build_schema_next_hop_result_read(cls._schema_on_200)

            return cls._schema_on_200


class _ShowNextHopHelper:
    """Helper class for ShowNextHop"""

    _schema_next_hop_result_read = None

    @classmethod
    def _build_schema_next_hop_result_read(cls, _schema):
        if cls._schema_next_hop_result_read is not None:
            _schema.next_hop_ip_address = cls._schema_next_hop_result_read.next_hop_ip_address
            _schema.next_hop_type = cls._schema_next_hop_result_read.next_hop_type
            _schema.route_table_id = cls._schema_next_hop_result_read.route_table_id
            return

        cls._schema_next_hop_result_read = _schema_next_hop_result_read = AAZObjectType()

        next_hop_result_read = _schema_next_hop_result_read
        next_hop_result_read.next_hop_ip_address = AAZStrType(
            serialized_name="nextHopIpAddress",
        )
        next_hop_result_read.next_hop_type = AAZStrType(
            serialized_name="nextHopType",
        )
        next_hop_result_read.route_table_id = AAZStrType(
            serialized_name="routeTableId",
        )

        _schema.next_hop_ip_address = cls._schema_next_hop_result_read.next_hop_ip_address
        _schema.next_hop_type = cls._schema_next_hop_result_read.next_hop_type
        _schema.route_table_id = cls._schema_next_hop_result_read.route_table_id


__all__ = ["ShowNextHop"]

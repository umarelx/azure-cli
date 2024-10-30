# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools   
# The fleet parameters are set in the Az cmd as -
#  az azure-fleet fleet create --resource-group rgazurefleet --fleet-name testFleet --spot-priority-profile "{capacity:20,min-capacity:10,max-price-per-vm:0.00865,eviction-policy:Delete,allocation-strategy:PriceCapacityOptimized,maintain:True}" --regular-priority-profile "{capacity:20,min-capacity:10,allocation-strategy:LowestPrice}" --vm-sizes-profile "[{name:Standard_d1_v2,rank:19225}]" --compute-profile "{base-virtual-machine-profile:{osProfile:{computerNamePrefix:o,adminUsername:nrgzqciiaaxjrqldbmjbqkyhntp,adminPassword:adfbrdxpv,customData:xjjib,windowsConfiguration:{provisionVMAgent:True,enableAutomaticUpdates:True,timeZone:hlyjiqcfksgrpjrct,additionalUnattendContent:[{passName:OobeSystem,componentName:Microsoft-Windows-Shell-Setup,settingName:AutoLogon,content:bubmqbxjkj}],patchSettings:{patchMode:Manual,enableHotpatching:True,assessmentMode:ImageDefault,automaticByPlatformSettings:{rebootSetting:Unknown,bypassPlatformSafetyChecksOnUserSchedule:True}},winRM:{listeners:[{protocol:Https,certificateUrl:'https://myVaultName.vault.azure.net/secrets/myCertName'}]},enableVMAgentPlatformUpdates:True},linuxConfiguration:{disablePasswordAuthentication:True,ssh:{publicKeys:[{path:kmqz,keyData:kivgsubusvpprwqaqpjcmhsv}]},provisionVMAgent:True,patchSettings:{patchMode:ImageDefault,assessmentMode:ImageDefault,automaticByPlatformSettings:{rebootSetting:Unknown,bypassPlatformSafetyChecksOnUserSchedule:True}},enableVMAgentPlatformUpdates:True},secrets:[{sourceVault:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}'},vaultCertificates:[{certificateUrl:'https://myVaultName.vault.azure.net/secrets/myCertName',certificateStore:nlxrwavpzhueffxsshlun}]}],allowExtensionOperations:True,requireGuestProvisionSignal:True},storageProfile:{imageReference:{publisher:mqxgwbiyjzmxavhbkd,offer:isxgumkarlkomp,sku:eojmppqcrnpmxirtp,version:wvpcqefgtmqdgltiuz,sharedGalleryImageId:kmkgihoxwlawuuhcinfirktdwkmx,communityGalleryImageId:vlqe,id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{imageName}/versions/{versionName}'},osDisk:{name:wfttw,caching:None,writeAcceleratorEnabled:True,createOption:FromImage,diffDiskSettings:{option:Local,placement:CacheDisk},diskSizeGB:14,osType:Windows,image:{uri:'https://myStorageAccountName.blob.core.windows.net/myContainerName/myVhdName.vhd'},vhdContainers:[tkzcwddtinkfpnfklatw],managedDisk:{storageAccountType:Standard_LRS,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'},securityProfile:{securityEncryptionType:VMGuestStateOnly,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'}}},deleteOption:Delete},dataDisks:[{name:eogiykmdmeikswxmigjws,lun:14,caching:None,writeAcceleratorEnabled:True,createOption:FromImage,diskSizeGB:6,managedDisk:{storageAccountType:Standard_LRS,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'},securityProfile:{securityEncryptionType:VMGuestStateOnly,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'}}},diskIOPSReadWrite:27,diskMBpsReadWrite:2,deleteOption:Delete}],diskControllerType:uzb},networkProfile:{healthProbe:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/probes/{probeName}'},networkInterfaceConfigurations:[{name:i,properties:{primary:True,enableAcceleratedNetworking:True,disableTcpStateTracking:True,enableFpga:True,networkSecurityGroup:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}'},dnsSettings:{dnsServers:[nxmmfolhclsesu]},ipConfigurations:[{name:oezqhkidfhyywlfzwuotilrpbqnjg,properties:{subnet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}'},primary:True,publicIPAddressConfiguration:{name:fvpqf,properties:{idleTimeoutInMinutes:9,dnsSettings:{domainNameLabel:ukrddzvmorpmfsczjwtbvp,domainNameLabelScope:TenantReuse},ipTags:[{ipTagType:sddgsoemnzgqizale,tag:wufmhrjsakbiaetyara}],publicIPPrefix:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIPPrefixName}'},publicIPAddressVersion:IPv4,deleteOption:Delete},sku:{name:Basic,tier:Regional}},privateIPAddressVersion:IPv4,applicationGatewayBackendAddressPools:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/backendAddressPools/{backendAddressPoolName}'}],applicationSecurityGroups:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName}'}],loadBalancerBackendAddressPools:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/backendAddressPools/{backendAddressPoolName}'}],loadBalancerInboundNatPools:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/inboundNatPools/{inboundNatPoolName}'}]}}],enableIPForwarding:True,deleteOption:Delete,auxiliaryMode:None,auxiliarySku:None}}],networkApiVersion:2020-11-01},securityProfile:{uefiSettings:{secureBootEnabled:True,vTpmEnabled:True},encryptionAtHost:True,securityType:TrustedLaunch,encryptionIdentity:{userAssignedIdentityResourceId:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{userAssignedIdentityName}'},proxyAgentSettings:{enabled:True,mode:Audit,keyIncarnationId:20}},diagnosticsProfile:{bootDiagnostics:{enabled:True,storageUri:'http://myStorageAccountName.blob.core.windows.net'}},extensionProfile:{extensions:[{name:bndxuxx,properties:{forceUpdateTag:yhgxw,publisher:kpxtirxjfprhs,type:pgjilctjjwaa,typeHandlerVersion:zevivcoilxmbwlrihhhibq,autoUpgradeMinorVersion:True,enableAutomaticUpgrade:True,settings:{},protectedSettings:{},provisionAfterExtensions:[nftzosroolbcwmpupujzqwqe],suppressFailures:True,protectedSettingsFromKeyVault:{secretUrl:'https://myvaultName.vault.azure.net/secrets/secret/mySecretName',sourceVault:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}'}}}}],extensionsTimeBudget:mbhjahtdygwgyszdwjtvlvtgchdwil},licenseType:v,scheduledEventsProfile:{terminateNotificationProfile:{notBeforeTimeout:iljppmmw,enable:True},osImageNotificationProfile:{notBeforeTimeout:olbpadmevekyczfokodtfprxti,enable:True}},userData:s,capacityReservation:{capacityReservationGroup:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}'}},applicationProfile:{galleryApplications:[{tags:eyrqjbib,order:5,packageReferenceId:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{applicationName}/versions/{versionName}',configurationReference:ulztmiavpojpbpbddgnuuiimxcpau,treatFailureAsDeploymentFailure:True,enableAutomaticUpgrade:True}]},hardwareProfile:{vmSizeProperties:{vCPUsAvailable:16,vCPUsPerCore:23}},serviceArtifactReference:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/serviceArtifacts/{serviceArtifactsName}/vmArtifactsProfiles/{vmArtifactsProfileName}'},securityPostureReference:{id:'/CommunityGalleries/{communityGalleryName}/securityPostures/{securityPostureName}/versions/{major.minor.patch}|{major.*}|latest',excludeExtensions:['{securityPostureVMExtensionName}'],isOverridable:True}},compute-api-version:2023-07-01,platform-fault-domain-count:1}" --zones "[zone1,zone2]" --identity "{type:UserAssigned,user-assigned-identities:{key9851:{}}}" --tags "{key3518:luvrnuvsgdpbuofdskkcoqhfh}" --location westus --plan "{name:jwgrcrnrtfoxn,publisher:iozjbiqqckqm,product:cgopbyvdyqikahwyxfpzwaqk,promotion-code:naglezezplcaruqogtxnuizslqnnbr,version:wa}"
# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------
"""
This module contains helper functions and test cases for managing Azure Compute Fleet resources.
Classes:
    FleetTestHelper: Provides methods to manage and test Azure Compute Fleet resources.
Methods:
    get_subnet_id(vnet): Extracts and returns the subnet ID from a given virtual network dictionary.
    test_get_subnet_id(): Tests the get_subnet_id method.
    generate_fleet_parameters(): Generates and returns parameters for creating a compute fleet.
    create_network_security_groups(): Creates a network security group and returns its ID.
    create_public_ip_address(): Creates a public IP address and returns its ID.
    create_nat_gateway(public_ip): Creates a NAT gateway using the provided public IP address and returns its ID.
"""
# --------------------------------------------------------------------------------------------
import json

class FleetTestHelper: 

    @staticmethod
    def generate_fleet_parameters(self, subscriptionId, resourceGroupName, location, public_ip_address_id):
        nat_gateway_id = FleetTestHelper.create_nat_gateway(self, public_ip_address_id, subscriptionId, resourceGroupName, location)
        network_security_groups_id = FleetTestHelper.create_network_security_groups(self, subscriptionId, resourceGroupName, location)
        adminUsername = "adminuser"
        
        addressSpaces = { "addressPrefixes": ["10.0.0.0/16"] }
        
        subnet = {
            "name": "subnetName",
            "properties": {
            "addressPrefix": "10.0.2.0/24",
            "networkSecurityGroup": {
                "id": network_security_groups_id
            },
            "natGateway": {
                "id": nat_gateway_id
            }
            }
        }
        
        subnets = [subnet]
        addressSpaces = {"addressPrefixes": ["10.0.0.0/16"]}

        input_data = {
            "location": location,
            "properties": {
                "addressSpace": addressSpaces,
                "subnets": subnets
            }
        }

        virtual_network_name = self.create_random_name('testVNet-', 32)
        virtual_network_id = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}"
        input_data_json = json.dumps(input_data)
        
        self.kwargs.update({
            'virtual_network_id':  virtual_network_id,
            'input_data_json': input_data_json,
            'location': location,
            'resource_group': resourceGroupName,
            'virtual_network_name': virtual_network_name
        })
        
        self.cmd(f'az network vnet create --name {virtual_network_name} --resource-group {resourceGroupName} --location {location} --subnet-name "subnet-fleet" --address-prefixes "10.0.0.0/16"  --subnet-prefixes "10.0.0.0/24"')
        
        spot_priority_profile = {
            "capacity": 3,
            "min_capacity": 2,
            "max_price_per_vm": 0.00865,
            "eviction_policy": "Delete",
            "allocation_strategy": "PriceCapacityOptimized",
            "maintain": False
        }

        regular_priority_profile = {
            "capacity": 3,
            "min_capacity": 2,
            "allocation_strategy": "LowestPrice"
        }
        vm_sizes_profile = [
            {"name": "Standard_D2s_v3", "rank": 19225},
            {"name": "Standard_D4s_v3", "rank": 1180}
        ]
        
        storageProfile = {
            "osDisk": {
                  "osType": "Linux",
                  "createOption": "FromImage",
                  "caching": "ReadWrite",
                  "managedDisk": {
                    "storageAccountType": "Standard_LRS"
                  },
                  "deleteOption": "Delete",
                  "diskSizeGB": 30
                },
            "imageReference": {
                  "publisher": "Canonical",
                  "offer": "UbuntuServer",
                  "sku": "16.04-LTS",
                  "version": "latest"
                }
        }
        
        compute_os_profile = {
                "osProfile": {
                    "computerNamePrefix": "o",
                    "adminUsername": adminUsername,
                    "linuxConfiguration": {
                        "disablePasswordAuthentication": True,
                        "ssh": {
                            "publicKeys": [
                                {
                                    "path": "home/{adminUsername}/.ssh/authorized_keys",
                                    "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+wWK73dCr+jgQOAxNsHAnNNNMEMWOHYEccp6wJm2gotpr9katuF/ZAdou5AaW1C61slRkHRkpRRX9FA9CYBiitZgvCCz+3nWNN7l/Up54Zps/pHWGZLHNJZRYyAB6j5yVLMVHIHriY49d/GZTZVNB8GoJv9Gakwc/fuEZYYl4YDFiGMBP///TzlI4jhiJzjKnEvqPFki5p2ZRJqcbCiF4pJrxUQR/RXqVFQdbRLZgYfJ8xGB878RENq3yQ39d8dVOkq4edbkzwcUmwwwkYVPIoDGsYLaRHnG+To7FvMeyO7xDVQkMKzopTQV8AuKpyvpqu0a9pWOMaiCyDytO7GGN you@me.com"
                                }
                            ]
                        }
                    }
                },
                "platformFaultDomainCount": 1,
                "computeApiVersion": "2023-09-01"
            }
        
        computeFleetVmssIPConfiguration = {
            "name": "internalIpConfig",
            "properties": {
                "subnet": {
                    "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{{virtualNetworkName}}/subnets/{{subnetName}}"
                    }
                    }
                }
        
        networkInterfaceConfiguration = {
                            "name": "exampleNic",
                            "properties": [
                                computeFleetVmssIPConfiguration
                            ],
                            "isPrimary": True,
                            "isAcceleratedNetworkingEnabled": False
        }
        
        networkProfile = {
            "networkInterfaceConfigurations": [
                networkInterfaceConfiguration
            ],
            "apiVersion": "2022-07-01"
        }
        
        computeProfile= {
            "apiVersion": "2023-09-01",
            "platformFaultDomainCount": 1,
            "baseVirtualMachineProfile": {
                "storageProfile": storageProfile,
                "networkProfile": networkProfile,
                "computeOsProfile": compute_os_profile
            }
        }
        
        computeFleetData = {
            "spot-priority-profile": spot_priority_profile,
            "vm-sizes-profile": vm_sizes_profile,
            "compute-profile": computeProfile,
            "regular-priority-profile": regular_priority_profile,
            "zones": ["1","2","3"],
            "tags": {"key3518": "luvrnuvsgdpbuofdskkcoqhfh"}
        }
        return computeFleetData

    @staticmethod
    def get_subnet_id(self, vnet):
        properties = vnet['properties']
        subnets = properties['subnets']
        subnet = subnets[0]
        return subnet['id']  
    
    @staticmethod
    def create_network_security_groups(self, subscriptionId, resourceGroupName, location):
        network_security_groups = self.create_random_name('testVNetNSG-', 32)
        network_security_groups_id = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{network_security_groups}"
        input_data = {
            "location": location
        }
        
        input_data_json = json.dumps(input_data)
        self.kwargs.update({
            'location': location,
            'input_data_json': input_data_json,
            'network_security_groups_id': network_security_groups_id,
            'resourceGroupName': resourceGroupName,
            'network_security_groups': network_security_groups
         })
        
        self.cmd(f'az network nsg create --resource-group {resourceGroupName} --name {network_security_groups} --location {location}')
        
        return network_security_groups_id

    def create_nat_gateway(self, public_ip, subscription_id, resource_group_name, location):
        nat_name = self.create_random_name('testFleetNatGW-', 34)
        nat_id = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/natGateways/{nat_name}"
        input_data = {
            "location": location,
            "sku": {"name": "Standard"},
            "properties": {
                "publicIpAddresses": [
                    {"id": public_ip}
                ]
            }
        }
          
        input_data_json = json.dumps(input_data)
        public_ip_json = json.dumps(public_ip)
        self.kwargs.update({
            'nat_id': nat_id,
            'input_data_json': input_data_json, # aupdate all jsons
            'location': location,
            'resource_group_name': resource_group_name,
            'nat_name': nat_name,
            'public_ip_json': public_ip_json
        })
        
        self.cmd(f'az network nat gateway create --resource-group {resource_group_name} --name  {nat_name} --location {location} --public-ip-addresses  \'{public_ip_json}\' --idle-timeout 4')
        return nat_id
#!/usr/bin/env python3
import base64
from aws_cdk import (
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elbv2,
    core,
)
vpc_id = 'vpc-0c97bc64'
security_grp = 'sg-0cd76560'
version = "versionone"
class TestingOnlyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

    # importing security Group from exesting resources
        mysg = ec2.SecurityGroup.from_security_group_id(self, "sg", security_group_id=security_grp)

    # importting Vpc from exesting resources
        vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id=vpc_id)

    # creating loadbalancer woth exesting resources
        lb = elbv2.ApplicationLoadBalancer(
            self, "LB",
            vpc=vpc,
            security_group=mysg,
            internet_facing=True, load_balancer_name= "myloadbalancer")

    # creating Target Group1
        mytarget_group = elbv2.ApplicationTargetGroup(self, "targetGroup", protocol=elbv2.ApplicationProtocol.HTTP, port=80, target_group_name="mytarget-group", vpc=vpc, health_check=elbv2.HealthCheck(enabled=True, healthy_http_codes="200", path="/", port="80"))

    # creating target group 2
        mytarget_group2 = elbv2.ApplicationTargetGroup(self, "targetGroup2", protocol=elbv2.ApplicationProtocol.HTTP, port=80, target_group_name="mytarget-group2", vpc=vpc, health_check=elbv2.HealthCheck(enabled=True, healthy_http_codes="200", path="/home", port="80"))

    # adding a loadbalancer default listener
        listener = lb.add_listener("listener", port=80, default_target_groups=[mytarget_group])

    # adding loadbalancer listener Rule
        if version == "versionone":
            slect_target = mytarget_group
        else:
            slect_target = mytarget_group2

        listenerRule = elbv2.ApplicationListenerRule(self, "listenerRule", listener=listener, priority=1, path_pattern="/home", target_groups=[slect_target])        
   
    # Output the DNS name of loadbalancer
        output_1 = core.CfnOutput(
            self,
            "mybucketoutput1",
            value=lb.load_balancer_dns_name,
            export_name="mybucketoutput1"
        )
        core.Tag.add(lb, "Name", "naresh")

        # The code that defines your stack goes here

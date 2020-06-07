#!/usr/bin/env python3

from aws_cdk import core

from testing_only.testing_only_stack import TestingOnlyStack

env_cn = core.Environment(account="521124255972", region="ap-south-1")


app = core.App()
TestingOnlyStack(app, "testing-only", env=env_cn)
core.Tag.add(app, key="UserID", value="yanduna")
core.Tag.add(app, key="AppID", value="pp4v")
core.Tag.add(app, key="Role", value="App")
app.synth()

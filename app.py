#!/usr/bin/env python3

from aws_cdk import core
import json

from testing_only.testing_only_stack import TestingOnlyStack
f = open('testing_only/test.json',)
data = json.load(f)

env_cn = core.Environment(account=data['account'], region=data['region'])


app = core.App()
TestingOnlyStack(app, "testing-only", env=env_cn)
core.Tag.add(app, key="UserID", value="yanduna")
core.Tag.add(app, key="AppID", value="pp4v")
core.Tag.add(app, key="Role", value="App")
app.synth()

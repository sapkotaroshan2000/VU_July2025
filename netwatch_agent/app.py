#!/usr/bin/env python3
from aws_cdk import App
from netwatch_agent.netwatch_agent_stack import NetWatchAgentStack  # match exact class name

app = App()
NetWatchAgentStack(app, "NetWatchAgentStack")
app.synth()

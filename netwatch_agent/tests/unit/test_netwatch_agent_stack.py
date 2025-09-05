import aws_cdk as core
import aws_cdk.assertions as assertions

from netwatch_agent.netwatch_agent_stack import NetwatchAgentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in netwatch_agent/netwatch_agent_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NetwatchAgentStack(app, "netwatch-agent")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

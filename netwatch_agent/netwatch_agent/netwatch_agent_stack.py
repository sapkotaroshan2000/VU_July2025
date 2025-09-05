from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_cloudwatch as cloudwatch,
)
from constructs import Construct

METRIC_NAMESPACE = "NetWatchMetrics"

class NetWatchAgentStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda function to run the site probe
        probe_lambda = _lambda.Function(
            self, "SiteProbeLambda",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="site_probe.handler",
            code=_lambda.Code.from_asset("lambda"),
            timeout=Duration.seconds(30),
            memory_size=256,
            description="Checks multiple sites and pushes metrics to CloudWatch"
        )

        # IAM permissions for CloudWatch metrics
        probe_lambda.add_to_role_policy(
            iam.PolicyStatement(
                actions=["cloudwatch:PutMetricData"],
                resources=["*"],
                conditions={"StringEquals": {"cloudwatch:namespace": METRIC_NAMESPACE}}
            )
        )

        # EventBridge schedule every 5 minutes
        schedule_rule = events.Rule(
            self, "FiveMinuteSchedule",
            schedule=events.Schedule.rate(Duration.minutes(5)),
            description="Invoke site probe Lambda every 5 minutes"
        )
        schedule_rule.add_target(targets.LambdaFunction(probe_lambda))

        # CloudWatch Dashboard
        dashboard = cloudwatch.Dashboard(
            self, "NetWatchDashboard",
            dashboard_name="NetWatchMetrics"
        )

        availability_metric = cloudwatch.Metric(
            namespace=METRIC_NAMESPACE,
            metric_name="Availability",
            statistic="Average",
            period=Duration.minutes(5)
        )

        latency_metric = cloudwatch.Metric(
            namespace=METRIC_NAMESPACE,
            metric_name="Latency",
            statistic="Average",
            period=Duration.minutes(5)
        )

        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Availability by Target",
                left=[availability_metric],
                width=12
            ),
            cloudwatch.GraphWidget(
                title="Latency (ms) by Target",
                left=[latency_metric],
                width=12
            )
        )

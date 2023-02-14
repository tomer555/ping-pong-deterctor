
from slack_sdk.webhook import WebhookClient

url = "https://hooks.slack.com/services/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"
webhook = WebhookClient(url)

def sendSlackMessage(status):
    if status == "FREE":
        webhook.send(
			text="Ping Pong Room Status",
			blocks=[
				{
					"type": "header",
					"text": {
						"type": "plain_text",
						"text": ":table_tennis_paddle_and_ball: Ping Pong Room Status :table_tennis_paddle_and_ball:"
					}
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": ":large_green_circle: :woman-running: The room is FREE! :runner: :large_green_circle:"
					}
				}
			]
		)
    else:
        webhook.send(
			text="Ping Pong Room Status",
            blocks=[
				{
					"type": "header",
                    "text": {
						"type": "plain_text",
                     	"text": ":table_tennis_paddle_and_ball: Ping Pong Room Status :table_tennis_paddle_and_ball:"
                    }
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
                    	"text": ":red_circle: The room is occupied :red_circle:"
                    }
				}
			]
		)
    print(f'slack message sent')

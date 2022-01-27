<div align="center">

# Messaging IoT Device state using AWS, Python and Telnyx

![Telnyx](/img/logo-dark.png)

An IoT use case where an IoT device sends data to the AWS cloud. And notifies anomaly to concerned individuals using Telnyx messaging.

</div>

## Prerequisite
 
 * [Telnyx Account](https://telnyx.com/sign-up?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link)
 * [Telnyx Phone Number](https://portal.telnyx.com/#/app/numbers/my-numbers?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link) enabled with:
    * [Telnyx Messaging Profile](https://portal.telnyx.com/#/app/messaging)
 * [Python](https://nodejs.org/en/) installed
 * [AWS](https://aws.amazon.com/) account
 * Raspberry Pi (optional)

  ## Steps

The following environmental variables need to be set

| Variable               | Description                                                                                                                                              |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TELNYX_API_KEY`       | Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link)              |
| `TELNYX_NUMBER`    | Your [Telnyx Public Key](https://portal.telnyx.com/#/app/account/public-key?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link) |
| `TELNYX_NUMBER`      | **Defaults to `8000`** The port the app will be served                                                                                                   |
| `AWS_END_POINT`             | Your **NGROK DOMAIN** like `"http://your-url.ngrok.io"`                                                                                                  |
| `CLIENT_ID` | The ID of the [call-control-connection](https://portal.telnyx.com/#/app/call-control/applications) to use for placing the calls                          |
| `THING_NAME` | The path to your google applications file |
| `THING_NAME.cert.pem` | The path to your google applications file |
| `THING_NAME.private.key` | The path to your google applications file |

 ### Step 1: Telnyx Setup 
 

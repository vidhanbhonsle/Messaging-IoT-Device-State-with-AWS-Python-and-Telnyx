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

The following values need to be replaced in publishData.py and lambda_function.py files

| Variable               | Description                                                                                                                                              |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TELNYX_API_KEY`       | Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link)              |
| `TELNYX_PHONE_NUMBER`    | Your [Telnyx number](https://portal.telnyx.com/#/app/numbers/my-numbers?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link) |
| `YOUR_PHONE_NUMBER`      | Your personal phone number                                                                                                   |
| `AWS_END_POINT`             | Your **NGROK DOMAIN** like `"http://your-url.ngrok.io"`                                                                                                  |
| `CLIENT_ID` | The ID of the Thing created                          |
| `THING_NAME` | The name of the Thing |
| `THING_NAME.cert.pem` | Downloaded from the connection kit |
| `THING_NAME.private.key` | Downloaded from the connection kit |

 ### Step 1: Telnyx Setup 
 

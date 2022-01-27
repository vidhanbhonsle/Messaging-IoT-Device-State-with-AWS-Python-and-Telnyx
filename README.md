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
| `AWS_END_POINT`             | Endpoint for communication with Thing using MQTT(works for HTTP too). Can be found under **`settings`** menu of **`AWS IoT`**                                                                                              |
| `CLIENT_ID` | The ID of the Thing created                          |
| `THING_NAME` | The name of the Thing |
| `THING_NAME.cert.pem` | Downloaded from the connection kit |
| `THING_NAME.private.key` | Downloaded from the connection kit |

 ### Step 1: Telnyx Setup 
Sign up for Telnyx account, obtain a number with SMS capabilities and configure the number for messaging.
If you already have a Telnyx number with messaging enabled you do not need to exapnd this step. 
<details>
<summary><strong>Steps to follow</strong> (click to expand)</summary><p>

 1. Sign up for Telnyx account
    > Set up a developer account with [Telnyx](https://telnyx.com/sign-up?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link).

 2. Obtain a number with SMS capabilities for auto-responder app
    > After creating an account and signing in, you need to [acquire a number](https://portal.telnyx.com/#/app/numbers/my-numbers?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link) for the application. Search for a number by selecting your preferred 'Region' or 'Area Code'.
    
    > Make sure that the number supports SMS feature(Very Important!) as it will be used by our application.
 
 3. Create a messaging profile
    > Next create a [messaging profile](https://portal.telnyx.com/#/app/messaging?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link) by clicking on "Add new profile" and provide a suitable profile name to it(you do not need to provide any other detail for now).

 4. Configure the number for messaging
    > Go to the [numbers](https://portal.telnyx.com/#/app/numbers/my-numbers??utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link) page, look for the number you created and set the number's `Messaging Profile` to the profile you created in the previous step. 
    
    <details>
    <summary>What if the Telnyx number is an international number for a User</summary>
    <br>    
    
    > If you want to send the message to a Telnyx number which is not in the country where you are, then you need to click on the 'Routing' option.
     <img src='./img/routing_click_red.png' width="800"/>
    
    > After clicking on 'Routing', a dialog box will open. In there, select the traffic type as "P2P" to allow International Inbound and Outbound SMS deliverability. And do not forget to save the changes!  

     <img src='./img/routing_selected.png' width="800"/> 
    </details>
    
 5. Acquire Telnyx API key
    > Go to the [API Keys](https://portal.telnyx.com/#/app/api-keys??utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link) page and copy the API Key for the future steps. Incase there is no API Key, then create one.

</p></details>
___

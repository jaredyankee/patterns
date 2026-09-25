// importing stripe
import Stripe from 'Stripe';
const stripe = new Stripe(process.env.stripe_api_key); // .env.example

/**
 *  Verifies you are the intended recipient. Show your credentials
 * 
 * @param {} event - emited from stripe webhook event
 * @returns - validated request body
 */
async function verifyStripeHook (event) {
    // test signature is header["stripe-signature"]
    let signature = event.headers["stripe-signature"];

    return await stripe.webhooks.constructEvent( 
        event.body,
        signature,
        process.env.stripe_webhook_secret // .env.example 
    )
}
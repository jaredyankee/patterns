// importing stripe
import Stripe from 'Stripe';
const stripe = new Stripe(process.env.stripe_api_key); // .env.example

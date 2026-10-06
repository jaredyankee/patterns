// cors.js
/**
 * Handles Access-Control-Allow-Origin headers for standard origin based requests
 * This is not secure but will resolve any issues with requests being denied by CORS policy
 * 
 * I have this function return type as variable; if it returns and object with 'statusCode', the caller knows to return right away
 *      otherwise it knows the request has passed CORS check
 */

export function CORS (event) {

    const allowedOrigins = process.env.allowed_origins.split(",") // asasumes that .env has comma delimited allowed origins
    
    // declare headers so they can be returned

    const headers = {
        "Access-Control-Allow-Origin": allowedOrigins.includes(event?.headers?.origin) ? event.headers.origin : "",
        "Access-Control-Allow-Methods": "GET, POST, PUT, PATCH, OPTIONS, DELETE", // your methods here
        "Access-Control-Allow-Headers": event?.headers["access-control-request-headers"] || "Content-Type",
        "Vary": "Origin"
    };
    
    if (event?.httpMethod == "OPTIONS") {
        return {
            statusCode: 200,
            headers: headers,
            body: JSON.stringify({
                message: "OPTIONS approved"
            })
        };
    }
    // return error if origin not in headers
    if (!allowedOrigins.includes(event?.headers?.origin)) {
        return {
            statusCode: 401,
            headers,
            body: JSON.stringify({
                message: "Unauthorized"
            })
        };
    }

    return headers; // now can use these headers in the eventual response

}
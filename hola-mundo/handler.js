
const hello = async (event, context) => {
    return {
        "statusCode": 200,
        "body": JSON.stringify({ 'message': 'Hola mundo - bienvenidos al curso de serverless framework en aws'})
    }
}

module.exports = {
    hello
}

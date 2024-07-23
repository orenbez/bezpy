# GraphQL is an open-source data query and manipulation language for APIs developed by Facebook in 2012 and released publicly in 2015
# It provides an approach to developing web APIs and has been compared and contrasted with REST and other web service architectures

# schema.gql -> response.json
# Can specify the requested fields from the API

# A GraphQL request can be either a query (read operation) or a mutation (write operation)
# https://www.apollographql.com/blog/graphql-vs-rest-5d425123e34b
# GraphQL vs REST API  https://www.youtube.com/watch?v=yWzKJPw_VzM

# use GraphQL queries and mutations to retrieve data from a database or other source.
# In a GraphQL API, you’re able to define the exact data you want from the server, and nothing more.
# GraphQL is a query language for APIs that was developed by Facebook and released as open-source software in 2015.

# The idea behind GraphQL is that instead of having multiple endpoints for each resource, you can have one endpoint (or URL) and ask for exactly what you need at that point in time.
# This is done by sending a query string with your request where it will be parsed by the server and returned as JSON or XML.

# GraphQL has many benefits over REST APIs, including:
# Flexible data requirements: You can specify exactly what data you need and only that data will be returned instead of having to make several requests to get just what you want.
# Efficient data usage: Data is sent only when required, saving bandwidth and increasing performance by reducing unnecessary roundtrips between client and server.
# Versioning support: If your API changes over time, your clients will not break because they know what version of the API they are using at any given time thanks to a query parameter in their requests.
# Strongly typed APIs: You don’t need to worry about casting strings



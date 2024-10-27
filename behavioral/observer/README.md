# Observer

The idea is quite simple: this pattern consists of a strategy to send messages to a list of interested observers. 
There is a publisher and a list of subscribers; the publisher sends a message to all subscribers. The main purpose is 
to avoid the need for the interested group of observers to check with the publisher about the state of some object.

Think about a store and a customer. The store will release a new version of a product, and the customer is very 
interested. Without this pattern, the customer needs to go to the store and check if the new version is available, 
even if the product has not been released yet, which wastes unnecessary resources for the customer and may cause 
congestion at the store to attend to all customers and provide feedback. With the pattern, the store will send a 
message to all interested customers only when the product is available, avoiding the need for the customer to go to 
the store and check if the product is available.
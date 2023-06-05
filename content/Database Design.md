---
aliases: []
date created: Jun 4th, 2023
date modified: Jun 4th, 2023
---

## Anomaly
1. **Insert Anomaly**: This occurs when certain attributes cannot be inserted into the database without the presence of other attributes. For example, in a table that stores both customer information and their orders, you wouldn't be able to insert a new customer until they have an order, and vice versa.
2. **Update Anomaly**: This occurs when the same piece of data is stored in multiple rows, and updating that data in one row can lead to inconsistent data. For example, if a customer's address is stored with each order they've made, and the customer moves, you'd need to update the address associated with each order. If some are missed, you can end up with different addresses for the same customer.
3. **Delete Anomaly**: This occurs when deleting a row inadvertently causes more data to be deleted than intended. For example, if a customer's information is stored in the same table as their orders, deleting an order might also delete the customer's information if that was their only order.

Normalization of the database schema, such as splitting the data into multiple, related tables, can help to reduce or eliminate these anomalies.
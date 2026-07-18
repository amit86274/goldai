
class OCOManager:
    def cancel_peer(self, client, triggered_ticket, linked_ticket):
        client.cancel_order(linked_ticket)
        return {"triggered": triggered_ticket, "cancelled": linked_ticket}

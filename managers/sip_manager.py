class SIPManager:
    def __init__(self):
        self.sips = []

    def add_sip(self, sip: SIP):
        self.sips.append(sip)

    def get_sip_by_name(self, sip_name: str):
        for sip in self.sips:
            if sip.sip_name == sip_name:
                return sip
        return None

    def get_total_investments(self):
        """Calculate the total amount invested across all SIPs."""
        return sum(sum(investment["amount"] for investment in sip.investments) for sip in self.sips)

    def get_total_expected_returns(self):
        """Calculate the total expected returns from all SIPs."""
        return sum(sip.calculate_expected_returns() for sip in self.sips)

    def get_sip_investments(self, sip_name: str):
        """Retrieve all investments made towards a specific SIP."""
        sip = self.get_sip_by_name(sip_name)
        if sip:
            return sip.investments
        return []

    def get_next_investment_due_for_sip(self, sip_name: str):
        """Get the next investment due date for a specific SIP."""
        sip = self.get_sip_by_name(sip_name)
        if sip:
            return sip.get_next_investment_date()
        return None
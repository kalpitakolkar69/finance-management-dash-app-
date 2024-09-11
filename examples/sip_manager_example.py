# Define an account to link the SIP payments
savings_account = Account(name="My Savings", account_type=AccountType.SAVINGS, balance=10000.0)

# Create an SIP
sip_investment = SIP(
    sip_name="Mutual Fund SIP",
    investment_amount=200.0,  # Monthly investment amount
    sip_type=SIPType.MUTUAL_FUND,  # Investment type
    start_date=datetime(2024, 1, 1),
    frequency=RecurringPeriod.MONTHLY,  # Monthly SIP
    account=savings_account,  # Linked to a savings account
    expected_return_rate=8.0  # 8% annual expected return
)

# Add SIP to SIPManager
sip_manager = SIPManager()
sip_manager.add_sip(sip_investment)

# Make an investment
sip_investment.make_investment(datetime(2024, 2, 1))

# Calculate total investments
total_investments = sip_manager.get_total_investments()
print(f"Total Investments: ${total_investments}")

# Calculate expected returns
expected_returns = sip_manager.get_total_expected_returns()
print(f"Expected Returns: ${expected_returns}")

# Check next SIP investment due date
next_investment_due = sip_manager.get_next_investment_due_for_sip("Mutual Fund SIP")
print(f"Next SIP Investment Due: {next_investment_due}")
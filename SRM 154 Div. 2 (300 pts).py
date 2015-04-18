class ProfitCalculator(object):

    def percent(self, items):
        paid_total = 0
        cost_total = 0
        for i in items:
            paid_total += float(i[0:6])
            cost_total += float(i[6:14])
        profit_float = paid_total - cost_total
        profit_percent = int(100 * (profit_float / paid_total))

        return profit_percent

print ProfitCalculator().percent(("012.99 008.73", "099.99 050.00", "123.45 101.07"))

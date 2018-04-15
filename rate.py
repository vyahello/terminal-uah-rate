import argparse
from datetime import date
from rate.currencies import InjectCurrency
from rate.dates import CustomDate
from rate.rates import ToUahRate

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Allow to get exchange rate of specific currency to `uah`.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--currency', '-c', type=str, required=True,
                        help="""Currency to interpret into `uah` exchange rate comparision.
                         For instance `usd` represents dollar currency.""")
    parser.add_argument('--date', '-d', type=str, action='store', default=str(date.today()),
                        help='Date should be in YYYY-MM-DD format. Default is today date.')
    args = parser.parse_args()

    ToUahRate(InjectCurrency(args.currency), CustomDate(args.date)).value()
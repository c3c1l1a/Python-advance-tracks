from runner.koan import *
from koan_labs.dictionary_practice import *

class  AboutDictionaryPractice(Koan):
	def test_dictionary_practice():
		"""
		This Activity is meant to give you more practice with dictionaries,lists and
		also a bit of sorting, i.e. the sorted() method in python. Think through the
		problem first before writing any code.My solution was 15 lines of code 
		but you are encouraged to write even more efficient code.Again, think through
		the problem before writing any code.

		_________
		ACTIVITY:
		_________
		You've been asked to help manage reports on how often people send and 
		receive money at Equity Bank.You're to write the method equity_tracker in koans labs
		which receives a list of transactions in the format, ["owen:susan:10", "owen:robert:10", "mark:drew:10"]
		Each item in the list is a transaction with the format of "from:to:amount"
		in the above transactions, owen sends susan 10 shillings, owen sends robert 10 shillings and
		mark sends drew 10 shillings. Make a list of strings that has each person who appears in
		any transaction with the net cash flow.E.g in the above example, return:
		[owen:-20,susan:10,mark:-10,robert:10,drew:10].Since Owen has sent 20 shillings
		and not received any money, his total is -20, etc. After You have calculated 
		the net flow of everyone and stored that information in a list, return a 
		list that is sorted alphabetically.

		in the example above, return [drew:10,mark:-10,owen:-20,robert:10,susan:10]

		"""
		self.assertEqual(equity_tracker(["adam:eve:123"]),['adam:-123.0', 'eve:123.0'],"Try Again")
		self.assertEqual(equity_tracker(["owen:susan:10", "owen:robert:10", "owen:drew:10"]),['drew:10.0', 'owen:-30.0', 'robert:10.0', 'susan:10.0'],"Try Again")
		self.assertEqual(equity_tracker(["fred:ricky:50", "ricky:fred:20", "fred:ethel:100", "ethel:fred:150.35"]),['ethel:-50.35', 'fred:20.35', 'ricky:30.0'],"Try Again")

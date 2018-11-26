class state
		def __init__(self, _accepting, _zero_tr, _one_tr)
			self.accepting = _accepting
			self.zero_tr = _zero_tr
			self.one_tr = _one_tr

class DFA
	def __init__(self)
		self.dfa = []

	def insert(self, state)
		self.dfa.insert(state)

class union
	def __init__ (self, dfa_1, dfa_2)
		var length_1 = len(dfa_1)
		var length_2 = len(dfa_2)
		self.union_table = [[0 for x in range(length_2)] for y in range(length_1)]
		for i in range(length_2):
			for j in range(length_1):
				self.union_table[i][j] = -1

	
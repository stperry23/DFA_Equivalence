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
		self.length_1 = len(dfa_1)
		self.length_2 = len(dfa_2)
		self.union_table = [[0 for x in range(length_2)] for y in range(length_1)]
		for row in range(length_2):
			for col in range(length_1):
				if (not dfa_1[col].state.accepting) and (not dfa_2[row].state.accepting):
					self.union_table[row][col] = -1
				else:
					self.union_table[row][col] = 1

def  union_main(dfa_1, dfa_2)
	table = union(dfa_1, dfa_2)
	for y in range(table.length_1):
		for x in range(table.length_2):
			table.union_table[x][y] = table.union_table[dfa_2[x].zero_tr][dfa_1[y].state.zero_tr]
			table.union_table[x][y] = table.union_table[dfa_2[x].one_tr][dfa_1[y].state.one_tr]


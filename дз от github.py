# s='aaabca'
# for sym in s:
#     count=0
#     for sub_sym in s:
#         if sub_sym==sym:
#             count+=1
#     print(sym, count)
# O(N)=N*N=N**2 итераций:4
# s='aabca'
# for sym in set(s): #set вытаскивает уникальные символы
#     count=0
#     for sub_sym in s:
#         if sub_sym==sym:
#             count+=1
#     print(sym, count)
# O(N)=M*N=N**2  итераций:6

# s='abc'
# syms_counter = {}
# for sym in s:
#     syms_counter[sym] = syms_counter.get(sym,0)+1
# print(syms_counter)
# # O(N) =git status

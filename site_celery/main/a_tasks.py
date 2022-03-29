# from celery import shared_task
#
#
# def count(fn):
#     count = 0
#     def raper(*args, **kwargs):
#         nonlocal count
#         count +=1
#         fn(*args)
#         print(count, 'count number')
#         return count
#     return raper
#
#
# # @shared_task
# # @count
# # def hello_oleg(name):
# #     print(f'hello {name}')
#
# @shared_task
# def hello_oleg(name):
#     print(f'hello {name}')
#
# hello_oleg=count(hello_oleg)

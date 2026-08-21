new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop(-1))

new_tasks.remove('task_007')

print('Новые таски:', new_tasks) # вывод измененного таска new_tasks
print('Завершенные таски:', completed_tasks) # вывод измененного таска completed_tasks
print('Последний таск:', new_tasks[-1]) # вывод последнего таска
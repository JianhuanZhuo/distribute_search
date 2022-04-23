import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)


def d_search():
    # 绑定端口5000, 设置验证码'mima123':
    manager = QueueManager(address=('', 4135), authkey=b'mima123')
    # 启动Queue:
    manager.start()
    task = manager.get_task_queue()

    for i in range(2):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')

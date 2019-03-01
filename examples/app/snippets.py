from myapp import *
from celery import chain, group, chord


chain_task = chain(
    print_task.si(val="t1"),
    print_task.si(val="t2"),
    print_task.si(val="t3"),
)

group_task = group(
    print_task.si(val="t1"),
    print_task.si(val="t2"),
    print_task.si(val="t3"),
)

chord_task = chord(
    [print_task.si(val="c_h1"), print_task.si(val="c_h2")]
)(print_task.si(val="c_c3"))

# t-g
tg_task = chain(
    print_task.si(val="t1"),
    group(
        print_task.si(val="g1"),
        print_task.si(val="g2"),
    )
)

# t-g-t
tg_task = chain(
    print_task.si(val="t1"),
    group(
        print_task.si(val="g1"),
        print_task.si(val="g2"),
    ),
    print_task.si(val="t2"),
)


# t-g-t-g-t . t-g()-t-g()-t
# final_task1 = celery.chain(
#     print_task.si(val="Starter task"),
#     celery.group([
#         print_task.si(val='group1, task1'),
#         print_task.si(val='group1, task2'),
#     ]),
#     print_task.si(val="group1, after-task"),
#     celery.group([
#         print_task.si(val='group2, task1'),
#         print_task.si(val='group2, task2'),
#     ]),
#     print_task.si(val="FINAL task"),
# )


# t-g-t-t-g-t . t-g()-t-t-g()-t
# final_task = celery.chain(
#     print_task.si(val="Starter task"),
#     celery.group([
#         print_task.si(val='group1, task1'),
#         print_task.si(val='group1, task2'),
#     ]),
#     print_task.si(val="group1, after-task"),
#     print_task.si(val="group1, after-task2"),  # <---- commenting this makes it work
#     celery.group([
#         print_task.si(val='group2, task1'),
#         print_task.si(val='group2, task2'),
#     ]),
#     print_task.si(val="FINAL task"),
# )
# r = final_task()
# print(r.get())


from celery import group, chain, chord
from myapp import add, echo

zzg = chain([
    echo.si('zjm chain'),
    group([
        chain([echo.si(11), echo.si(12), echo.si(13)]),
        chain([echo.si(21), echo.si(22), echo.si(23)]),
    ]),
    echo.si('done')
])
result = zzg.apply_async()
print(result.get())

################################################################################

zjm2 = chain([
    echo.si('zjm chain'),
    group([
        chord(([echo.si(11), echo.si(12), echo.si(13)]), echo.si('aa')),
        chord(([echo.si(21), echo.si(22), echo.si(23)]), echo.si('bb')),
    ]),
    echo.si('done')
])
result = zjm2.apply_async()
print(result.get())


zjm1 = chain([
    echo.si('zjm chain'),
    group([
        chain(group([echo.si(11), echo.si(12), echo.si(13)]), echo.si('aa')),
        chain(group([echo.si(21), echo.si(22), echo.si(23)]), echo.si('bb')),
    ]),
    echo.si('done')
])
result = zjm1.apply_async()
print(result.get())


zjm2 = chain([
    echo.si('zjm chain'),
    # chain([
        chain(group([echo.si(11), echo.si(12), echo.si(13)]), echo.si('aa')),
        chain(group([echo.si(21), echo.si(22), echo.si(23)]), echo.si('bb')),
    # ]),
    echo.si('done')
])
result = zjm2.apply_async()
print(result.get())


mytasks_implicit = chain([
    echo.si('-> implicit chord'),
    # group([
    #     chain([
    #         group([
    #             chain([group([echo.si('111'), echo.si('112'), ]), echo.si('11_'), ]),
    #             chain([group([echo.si('121'), echo.si('122'), ]), echo.si('12_'), ]),
    #         ]), echo.si('1_'),
    #     ]),
    #     chain([
    #         group([
    #             chain([group([echo.si('211'), echo.si('212'), ]), echo.si('21_'), ]),
    #             chain([group([echo.si('221'), echo.si('222'), ]), echo.si('22_'), ]),
    #         ]), echo.si('2_'),
    #     ]),
    # ]),
    echo.si('_'),
    echo.si('#'),
    echo.si('$'),
])

mytasks_explicit = chain([
    echo.si('-> explicit chord'),
    chord([
        chord([
            chord([echo.si('111'), echo.si('112'), ], body=echo.si('11_')),
            chord([echo.si('121'), echo.si('122'), ], body=echo.si('12_')),
        ], body=echo.si('1_')),
        chord([
            chord([echo.si('211'), echo.si('212'), ], body=echo.si('21_')),
            chord([echo.si('221'), echo.si('222'), ], body=echo.si('22_')),
        ], body=echo.si('2_')),
    ], body=echo.si('_')),
    echo.si('#'),
    echo.si('$'),
])

mytasks_or_operator = echo.si('-> or operator') | group([
    group([
        group([echo.si('111'), echo.si('112'), ]) | echo.si('11_'),
        group([echo.si('121'), echo.si('122'), ]) | echo.si('12_'),
    ]) | echo.si('1_'),
    group([
        group([echo.si('211'), echo.si('212'), ]) | echo.si('21_'),
        group([echo.si('221'), echo.si('222'), ]) | echo.si('22_'),
    ]) | echo.si('2_'),
]) | echo.si('_') | echo.si('#') | echo.si('$')

mytasks_implicit_3 = chain([
    echo.si('-> implicit chord (3)'),
    group([
        chain([
            group([
                chain([group([echo.si('111'), echo.si('112'), ]), echo.si('11_'), ]),
                chain([group([echo.si('121'), echo.si('122'), ]), echo.si('12_'), ]),
            ]), echo.si('1_'),
        ]),
        chain([
            group([
                chain([group([echo.si('211'), echo.si('212'), ]), echo.si('21_'), ]),
                chain([group([echo.si('221'), echo.si('222'), ]), echo.si('22_'), ]),
            ]), echo.si('2_'),
        ]),
        chain([
            group([
                chain([group([echo.si('311'), echo.si('312'), ]), echo.si('31_'), ]),
                chain([group([echo.si('321'), echo.si('322'), ]), echo.si('32_'), ]),
            ]), echo.si('3_'),
        ]),
    ]),
    echo.si('_'),
    echo.si('#'),
    echo.si('$'),
])

mytasks_explicit_3 = chain([
    echo.si('-> explicit chord (3)'),
    chord([
        chord([
            chord([echo.si('111'), echo.si('112'), ], body=echo.si('11_')),
            chord([echo.si('121'), echo.si('122'), ], body=echo.si('12_')),
        ], body=echo.si('1_')),
        chord([
            chord([echo.si('211'), echo.si('212'), ], body=echo.si('21_')),
            chord([echo.si('221'), echo.si('222'), ], body=echo.si('22_')),
        ], body=echo.si('2_')),
        chord([
            chord([echo.si('311'), echo.si('312'), ], body=echo.si('31_')),
            chord([echo.si('321'), echo.si('322'), ], body=echo.si('32_')),
        ], body=echo.si('3_')),
    ], body=echo.si('_')),
    echo.si('#'),
    echo.si('$'),
])

mytasks_or_operator_3 = echo.si('-> or operator (3)') | group([
    group([
        group([echo.si('111'), echo.si('112'), ]) | echo.si('11_'),
        group([echo.si('121'), echo.si('122'), ]) | echo.si('12_'),
    ]) | echo.si('1_'),
    group([
        group([echo.si('211'), echo.si('212'), ]) | echo.si('21_'),
        group([echo.si('221'), echo.si('222'), ]) | echo.si('22_'),
    ]) | echo.si('2_'),
    group([
        group([echo.si('311'), echo.si('312'), ]) | echo.si('31_'),
        group([echo.si('321'), echo.si('322'), ]) | echo.si('32_'),
    ]) | echo.si('3_'),
]) | echo.si('_') | echo.si('#') | echo.si('$')

# two "tasks" in main chord

result = mytasks_implicit.apply_async()
print(result.get())
time.sleep(1.5)

result = mytasks_explicit.apply_async()
print(result.get())
time.sleep(1.5)

result = mytasks_or_operator.apply_async()
print(result.get())
time.sleep(1.5)

# three "tasks" in main chord

result = mytasks_implicit_3.apply_async()
print(result.get())
time.sleep(1.5)

result = mytasks_explicit_3.apply_async()
print(result.get())
time.sleep(1.5)

result = mytasks_or_operator_3.apply_async()
print(result.get())

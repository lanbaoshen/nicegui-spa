from nicegui import ui


class DashboardPage:
    def __init__(self):
        self.age_panel = ui.echart(
            {
                'title': {'text': "Lanbao's Age"},
                'tooltip': {'trigger': 'axis', 'axisPointer': {'type': 'shadow'}},
                'xAxis': {
                    'type': 'category',
                    'data': list(range(1998, 2026)),
                    'axisLabel': {'interval': 0},
                },
                'yAxis': {
                    'type': 'value',
                    'splitNumber': 3,
                },
                'series': [{'type': 'line', 'data': list(range(28))}],
                'dataZoom': [
                    {
                        'type': 'slider',
                        'xAxisIndex': 0,
                        'start': 25,
                        'end': 75,
                    }
                ],
            },
            theme={
                'color': ['#4ea397', '#22c3aa', '#7bd9a5'],
            },
        )

        self.age_panel = ui.echart(
            {
                'title': {'text': "Lanbao's Work Experience"},
                'tooltip': {'trigger': 'axis', 'axisPointer': {'type': 'shadow'}},
                'xAxis': {
                    'type': 'category',
                    'data': list(range(2020, 2026)),
                    'axisLabel': {'interval': 0},
                },
                'yAxis': {
                    'type': 'value',
                    'splitNumber': 3,
                },
                'series': [{'type': 'line', 'data': list(range(6))}],
                'dataZoom': [
                    {
                        'type': 'slider',
                        'xAxisIndex': 0,
                        'start': 25,
                        'end': 75,
                    }
                ],
            },
            theme={
                'color': ['#4ea397', '#22c3aa', '#7bd9a5'],
            },
        )

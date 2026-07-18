
class RealtimeCharts:
    def update(self, series, value):
        series.append(value)
        return series

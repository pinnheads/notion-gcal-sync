from gcsa.event import Event
from gcsa.reminders import EmailReminder, PopupReminder
from gcsa.recurrence import Recurrence
from datetime import datetime
from random import randint

# days of the week
from gcsa.recurrence import SU, MO, TU, WE, TH, FR, SA

# possible repetition frequencies
from gcsa.recurrence import SECONDLY, MINUTELY, HOURLY, \
    DAILY, WEEKLY, MONTHLY, YEARLY


def convert_freq_day(freq=None):
    reference = {
        "DAILY": DAILY, "WEEKLY": WEEKLY, "MONTHLY": MONTHLY, "YEARLY": YEARLY, "SECONDLY": SECONDLY,
        "MINUTELY": MINUTELY, "HOURLY": HOURLY, "SU": SU, "MO": MO, "TU": TU, "WE": WE, "TH": TH, "FR": FR, "SA": SA
    }
    if freq is not None:
        try:
            return reference.get(freq)
        except KeyError:
            raise ValueError(f'Wrong Value provided for conversion function {freq}')
    else:
        raise ValueError('Provide a value for conversion')


def convert_datetime(date_str=None):
    if date_str:
        return datetime.fromisoformat(date_str)
    else:
        return datetime.now()


class TaskToEvent:
    def __init__(self, task):
        self.url = task.get('notion_url')
        self.notion_id = task.get('_id')
        self.notion_id_field = task.get('notion_id')
        self.action = task.get('action')
        self.recurring_task = task.get('recurring_task?')
        self.reminders = task.get('reminders')
        self.status = task.get('status')
        self.date = task.get('date')
        self.gcal_id_field = task.get('gcal_id')
        self.minutes_before_email_reminder = task.get('minutes_before_email_reminder') or 60
        self.minutes_before_popup_reminder = task.get('minutes_before_popup_reminder') or 10
        self.interval = task.get('interval')
        self.by_month = task.get('by_month')
        self.by_week_day = task.get('by_week_day')
        self.count = task.get('count')
        self.task_category = task.get('task_category')
        self.description = ""
        self.frequency = task.get('frequency')
        self.title = f"{task.get('title')} - {self.status}" if self.status is not None else task.get('title')
        for _ in task.get('description'):
            self.description += _

    def create_reminder(self):
        reminders = []
        if self.reminders:
            for reminder in self.reminders:
                if reminder.lower() == "email":
                    reminders.append(EmailReminder(minutes_before_start=self.minutes_before_email_reminder))
                elif reminder.lower() == "popup":
                    reminders.append(PopupReminder(minutes_before_start=self.minutes_before_popup_reminder))
                else:
                    reminders.append(PopupReminder(minutes_before_start=10))
        else:
            reminders.append(PopupReminder(minutes_before_start=10))
        return reminders

    def create_recurrence(self):
        if self.recurring_task:
                by_month = self.by_month if self.by_month is not None and self.by_month < 13 else None
                count = self.count
                interval = self.interval
                by_days = [convert_freq_day(day) for day in self.by_week_day]
                freq = convert_freq_day(self.frequency) if self.frequency != "CUSTOM" else None
                if freq is not None:
                    return [Recurrence.rule(freq=freq, by_week_day=by_days, by_month=by_month, count=count, interval=interval)]
                return [Recurrence.rule(by_week_day=by_days, by_month=by_month, count=count, interval=interval)]
        else:
            return []

    def create_event(self) -> Event:
        if self.task_category.lower() == "personal":
            color = randint(1, 10)
        elif self.task_category.lower() == "work":
            color = 11
        else:
            color = randint(1, 10)
        if self.date is not None:
            return Event(summary=f"{self.title}",
                         start=convert_datetime(self.date.get('start')),
                         end=convert_datetime(self.date.get('end')) or None,
                         timezone="Asia/Calcutta",
                         description=f"notion_id: {self.notion_id}\nnotion_url: {self.url}\n{self.description}",
                         recurrence=self.create_recurrence(),
                         color_id=color,
                         reminders=self.create_reminder(),
                         default_reminders=False,
                         )
        return Event(summary=self.title,
                     start=convert_datetime(date_str=datetime.today().strftime('%Y-%m-%d')),
                     timezone="Asia/Calcutta",
                     description=f"notion_id: {self.notion_id}\nnotion_url: {self.url}\n{self.description}",
                     recurrence=self.create_recurrence(),
                     color_id=color,
                     reminders=self.create_reminder(),
                     default_reminders=False,
                     )
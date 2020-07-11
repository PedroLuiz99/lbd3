SELECT event.event_id,
       event.user_id,
       event.event_name,
       event.event_description,
       event.date_start,
       event.date_end,
       event.active
FROM   event
WHERE  event.user_id = %s
       AND event.active = 1
       AND (
			event.date_start < DS AND event.date_end >= DS
			OR event.date_start >= DS AND event.date_end <= DE
			OR event.date_start > DS AND event.date_end < DE
			OR event.date_start <= DE AND event.date_end > DE
		)

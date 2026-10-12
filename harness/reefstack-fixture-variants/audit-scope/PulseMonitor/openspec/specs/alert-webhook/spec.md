# alert-webhook Specification

## Purpose
Outbound alerts for salinity events.

## Requirements

### Requirement: Webhook on salinity events
The daemon SHALL post a JSON alert to the configured webhook URL within 30 seconds of a
salinity event.

#### Scenario: An event fires
- **WHEN** a salinity event is detected
- **THEN** one POST reaches the webhook URL with the event's start time and peak value

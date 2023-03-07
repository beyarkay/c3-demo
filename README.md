# Custom Calendar Creator demo project

See [the main repo](https://github.com/beyarkay/c3) for details

## Getting started

Once you've used this repo as a template, these are the steps you need to go
through in order to get your custom data in your calendar:

- [ ] Edit the code in `create-calendars.py` to grab your own data and write it
  out to a file in the `calendars/` directory (see `create-calendars.py` for an
  example)

- [ ] (optional) Update `.github/workflows/create-calendars.yaml` with your own
  schedule for when you want GitHub to run your script. This is useful for
  customising when you want your calendar to be updated with the latest
  information. You'll see there's a `cron` line that looks like:

  ```
  on:
    schedule:
      - cron: '0 0 * * *' # every day at midnight
  ```

  You want to change the `cron:` string to a string describing your schedule,
  in cron-notation. Use https://cron.help to get some help in this regard.

- [ ] In `.github/workflows/create-calendars.yaml`, change the name of the
  script from `My Cool Calendar Creator` to something more descriptive.

  ```diff
    # The name of this workflow
-   name: My Cool Calendar Creator
+   name: Something more descriptive
  ```

- [ ] Also in `.github/workflows/create-calendars.yaml`, change the body of the
  release to be something that describes your project a bit better.

  ```diff
    - name: Update latest release with new calendars
      ...
      with:
        ...
-       body: "This is an example release showing how you can publish internet
-         calendars that are available via github. Simply copy one of the links
-         to the files below into your calendar app and you'll get all the
-         latest updates as they happen!"
+       body: "A more descriptive body"
  ``

- [ ] Remove everything in this README, and replace it with something that
  describes your project a bit better.

## YAML calendar format

It is expected that the calendar files (by default matching `calendars/*.yaml`)
have a specific format:

1. Each file in `calendars/` will be turned into a single ICS file with the
   same name but with the extension `.ics`. So `calendars/simple-calendar.yaml`
   will become `calendars/simple-calendar.ics`. These `.ics` files will then be
   published.

   If you want multiple calendars, create multiple YAML files.

2. Each `.yaml` file should contain a list under the key `events`. Other keys
   may be added in the future.

3. Each of the items in the `events` list should be a single event, with
   different keys and values which will be mapped to single calendar events.

For example, this will create a single calendar with one event:

```yaml
events:
  - start: 2022-01-01T08:00:00.0000
    end: 2022-01-01T10:00:00.0000
    title: 'Happy new year!',
    description: 'This event was created by [c3](https://github.com/beyarkay/c3)',
```

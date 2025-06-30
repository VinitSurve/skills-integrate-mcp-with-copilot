# Managing Activities

## For Teachers: How to Add, Edit, or Remove Activities

The activities for the Mergington High School website are now stored in a simple file called `activities.json` located in the `src` folder. You no longer need to modify the Python code to manage activities!

### How to Edit Activities

1. Open the file `src/activities.json` in any text editor
2. Make your changes following the format below
3. Save the file
4. The website will automatically use your changes

### Activity Format

Each activity follows this structure:

```json
"Activity Name": {
  "description": "Brief description of the activity",
  "schedule": "When the activity meets (e.g., 'Mondays, 3:30 PM - 4:30 PM')",
  "max_participants": 15,
  "participants": ["email1@mergington.edu", "email2@mergington.edu"]
}
```

### Examples

#### Adding a New Activity
To add a new activity, add it to the activities.json file:

```json
"Robotics Club": {
  "description": "Build and program robots for competitions",
  "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
  "max_participants": 16,
  "participants": []
}
```

#### Changing Activity Details
Simply edit the values in the existing activity:

```json
"Chess Club": {
  "description": "Learn strategies and compete in chess tournaments - now with weekly tournaments!",
  "schedule": "Fridays, 3:30 PM - 5:00 PM",
  "max_participants": 15,
  "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
}
```

#### Removing an Activity
Delete the entire activity block from the file. Make sure to remove the comma if it's the last item.

### Important Notes

- **Always make a backup** of the file before making changes
- **Check your formatting** - make sure you don't accidentally delete commas, quotes, or brackets
- **Student emails** in the "participants" list should always end with "@mergington.edu"
- **Max participants** should be a number (no quotes around it)
- **All other fields** should be in quotes

### Need Help?

If you accidentally break the file format, the website will show an error. Contact the IT department or restore from your backup copy.

The original activities are preserved in the code comments if you need to reference them.

"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
import json
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# Function to load activities from JSON file
def load_activities():
    """Load activities from the activities.json file"""
    activities_file = current_dir / "activities.json"
    try:
        with open(activities_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {activities_file} not found. Using empty activities dictionary.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error parsing {activities_file}: {e}")
        return {}

# Function to save activities to JSON file
def save_activities(activities_data):
    """Save activities to the activities.json file"""
    activities_file = current_dir / "activities.json"
    try:
        with open(activities_file, 'w', encoding='utf-8') as f:
            json.dump(activities_data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving activities to {activities_file}: {e}")
        return False

# Load activities on startup
activities = load_activities()


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    # Reload activities to ensure we return the latest data
    return load_activities()


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Reload activities to get latest data
    global activities
    activities = load_activities()
    
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Student is already signed up"
        )

    # Add student
    activity["participants"].append(email)
    
    # Save changes back to file
    if not save_activities(activities):
        raise HTTPException(status_code=500, detail="Failed to save changes")
    
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str):
    """Unregister a student from an activity"""
    # Reload activities to get latest data
    global activities
    activities = load_activities()
    
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is signed up
    if email not in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Student is not signed up for this activity"
        )

    # Remove student
    activity["participants"].remove(email)
    
    # Save changes back to file
    if not save_activities(activities):
        raise HTTPException(status_code=500, detail="Failed to save changes")
    
    return {"message": f"Unregistered {email} from {activity_name}"}

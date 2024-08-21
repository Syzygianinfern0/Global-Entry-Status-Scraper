# Global-Entry-Status-Scraper
Monitor the current processing status of your Global Entry Application from https://portal3.passportindia.gov.in

## Usage
1. Clone the repository
2. Run goes.py with your application number as an argument
```bash
python goes.py --arn <application_number>
```
3. The script will output the current status of your application. Example:
```
2024-MM-DD: PVR SCAN AND UPLOADED SUCCESSFULLY
2024-MM-DD: Approved and Submitted as Clear by Police
2024-MM-DD: Application Granted on pre police verification basis
2024-MM-DD: Sent To Go
2024-MM-DD: Background Verification Form for GEP Submitted
```

Reference: https://www.reddit.com/r/GlobalEntry/comments/1ci37e7/steps_to_check_the_current_detailed_status_for/

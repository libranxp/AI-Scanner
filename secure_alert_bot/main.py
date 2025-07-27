import os
from secure_alert_bot.scheduler import run_scheduler

def main():
    # Ensure all required environment variables are set
    required_env_vars = [
        'TELEGRAM_BOT_TOKEN',
        'PENNY_STOCK_CHANNEL_ID',
        'STOCK_CHANNEL_ID',
        'CRYPTO_CHANNEL_ID'
    ]

    for var in required_env_vars:
        if var not in os.environ:
            raise EnvironmentError(f"Missing required environment variable: {var}")

    # Start the scheduler to send alerts
    run_scheduler()

if __name__ == "__main__":
    main()

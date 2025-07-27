import os
from secure_alert_bot.scheduler import run_scheduler


def validate_env_vars():
    required_env_vars = [
        'TELEGRAM_BOT_TOKEN',
        'PENNY_STOCK_CHANNEL_ID',
        'STOCK_CHANNEL_ID',
        'CRYPTO_CHANNEL_ID',
        'FMP_API_KEY'
    ]

    missing_vars = [var for var in required_env_vars if var not in os.environ]
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")


def main():
    print("Validating environment variables...")
    validate_env_vars()

    print("Starting alert scheduler...")
    run_scheduler()


if __name__ == "__main__":
    main()

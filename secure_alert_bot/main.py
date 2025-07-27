import os
from secure_alert_bot.scheduler import run_scheduler
from logger import get_logger


def main():
    logger = get_logger("secure_alert_bot", log_file="logs/bot.log")

    # Ensure all required environment variables are set
    required_env_vars = [
        'TELEGRAM_BOT_TOKEN',
        'PENNY_STOCK_CHANNEL_ID',
        'STOCK_CHANNEL_ID',
        'CRYPTO_CHANNEL_ID',
        'FMP_API_KEY'
    ]

    missing_vars = [var for var in required_env_vars if var not in os.environ]
    if missing_vars:
        for var in missing_vars:
            logger.error(f"Missing required environment variable: {var}")
        raise EnvironmentError(f"Missing environment variables: {', '.join(missing_vars)}")

    logger.info("Starting the secure alert bot scheduler...")
    try:
        run_scheduler()
    except Exception as e:
        logger.exception("Failed to start the scheduler")
        raise e


if __name__ == "__main__":
    main()


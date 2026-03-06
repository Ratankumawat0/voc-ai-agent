from database.db import create_table
from scraper.scraper import scrape_reviews
from reports.global_report import generate_global_report
from reports.weekly_report import generate_weekly_report
from agent.query_agent import ask_agent

def run_agent():

    print("AI Agent Running")

    create_table()

    scrape_reviews()

    generate_global_report()

    generate_weekly_report()

    print("Agent completed")

if __name__ == "__main__":

    run_agent()

    ask_agent("battery issues")
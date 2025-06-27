import datetime
from backend.calendar_utils import parse_datetime_from_text, check_availability, create_event
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent
from langchain.agents.agent import AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain_core.tools import tool

@tool
def book_meeting(input: str) -> str:
    """Book a meeting based on natural language input like 'tomorrow afternoon' or 'next Friday 3pm'."""
    dt = parse_datetime_from_text(input)
    if not dt:
        return "❌ Sorry, I couldn't understand the date/time you mentioned. Please try again."

    start_time = dt
    end_time = dt + datetime.timedelta(hours=1)

    if not check_availability(start_time, end_time):
        return "❌ That time is already booked. Please choose another."

    link = create_event("Scheduled Meeting", start_time, end_time)
    return f"✅ Your meeting is booked! Join link: {link}"

def run_conversation(user_input):
    try:
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        tools = [book_meeting]

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You're a helpful assistant that schedules meetings for the user."),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])

        agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)
        executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

        result = executor.invoke({"input": user_input})
        return result.get("output", "❌ No output from AI agent.")
    except Exception as e:
        return f"❌ run_conversation error: {str(e)}"
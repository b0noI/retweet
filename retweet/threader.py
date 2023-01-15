import os
import openai

from . import const 
from . import utils
from . import templates


def rethread(text):
    template = templates.get_other_template("twitter-threader-v0")
    prompt = template.substitute(text=text)
    prompt_length = len(prompt)
    output_size = 4000 - prompt_length - 1
    openai.organization = const.GPT3_ORG_ID
    openai.api_key = utils.get_gpt3_secret()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=output_size,
        temperature=0.9
    )
    return response["choices"][0]["text"].strip()

if __name__ == "__main__":
    print(
        rethread(
            """It is interesting how many people do not realize the differences between levels in big companies in silicon valley and outside. More or less, they go like this:
L3 - Junior
L4 - Middle
L5 - Senior
L6 - Staff
L7 - Sr. Staff
L8 - Director
L9 - Sr. Director
L10 - VP

This is very close to Google levels, you can see matching on other companies at level http://levels.fyi , but you got the point. They are more or less universal across big tech companies. It is beneficial since you know precisely at which level you will be hired at another company (or, at least, what your level is there).

These levels are not arbitrary. They mean concrete things. For leaders: they indicate how many people report to you. For example, L7 probably, on average, will have 20+ at a starting point, L6 might be first-level manager, and seldom will you see L5 as a manager. Levels also mean the salary band you are in (you want your seven figures, you must be at least L7).

However at startup, things are entirely different. I have seen way too many CTOs who, at best, can pass L5-level interivew. In a startup, levels mean a completely different thing. They mean inspirationally where you can be if startup will win. Similar how startup RSUs mean potential money (not real money today), level mean potential scope, not real scope today. L8 in startup very likely migth have scope equal to L4 in big tech, but if startup if succesfull it will be real L8, with real money and a really big scope.
And in some cases, even bigger than contrerpiar from big company. But it is not real at the moment. So, keep all these in mind if you are going to a 40ppl startup as a Director, are you truly belive the startup will be succesfull? since if not it is not only money that will never materialize, it is your level as will never materialize to actual L8.
            """
            )
    )

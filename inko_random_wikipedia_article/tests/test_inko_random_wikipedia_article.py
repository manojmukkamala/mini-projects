from inko_random_wikipedia_article import build_user_agent

def test_build_user_agent():
    assert "inko-random-wikipedia-article" in build_user_agent()
    assert "Contact:" in build_user_agent()
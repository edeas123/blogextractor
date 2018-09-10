
from blogextractor.extractors.page import NairalandForumPageExtractor
from blogextractor.extractors.forum import NairalandForumExtractor
from blogextractor.extractors.topic import NairalandTopicExtractor


# use a factory function to return the appropriate extractor class
def get_extractor(blog, type):
    if not blog:
        # TODO: throw an appropriate error or exception
        # e.g. value error
        return

    return {
        'nairaland':
            {
                'forum': NairalandForumExtractor,
                'page': NairalandForumPageExtractor,
                'topic': NairalandTopicExtractor
            }
    }[blog][type]


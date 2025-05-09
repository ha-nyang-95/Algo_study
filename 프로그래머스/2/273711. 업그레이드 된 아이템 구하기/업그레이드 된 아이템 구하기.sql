# PARENT_ITEM_ID가 ITEM_INFO 테이블에서 ITEM_ID와 같을 때,
# PARITY가 RARE인 값들만 선별
# 선별한 값들의 ITEM_TREE 테이블의 ITEM_ID와 ITEM_INFO 의 테이블의 ITEM_ID가
# 일치하는 값들만 선택하여 테이블을 구성

SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID IN (
                SELECT T.ITEM_ID
                FROM ITEM_INFO I, ITEM_TREE T
                WHERE I.ITEM_ID = T.PARENT_ITEM_ID AND I.RARITY='RARE'
                )
ORDER BY ITEM_ID DESC
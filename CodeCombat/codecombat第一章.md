# CodeCombat-第一章
~~过于简单的就不提了~~
~~收费的也没有玩过~~
~~在[CodeCombat中国](http://www.codecombat.cn/ "CodeCombat中国")上玩的~~
~~关卡名称也是按上面写的，语言用的lua~~
## KITHGARD地牢
    self:moveRight()
    self:moveDown()
    self:moveRight()

## 深藏的宝石
    self:moveRight()
    self:moveRight()
    self:moveUp()
    self:moveLeft()
    self:moveDown()
    self:moveDown()

## 幽灵守卫
    self:moveRight()
    self:moveUp()
    self:moveRight()
    self:moveDown()
    self:moveRight()

## 健忘的宝石匠
    self:moveRight()
    self:moveUp()
    self:moveRight()
    self:moveRight()
    self:moveDown()
    self:moveDown()
    self:moveUp()
    self:moveRight()

## 不详的征兆
    self:moveRight()
    self:moveDown()
    self:moveUp()
    self:moveRight()
    self:moveUp()
    self:moveRight()
    self:moveRight()
    self:moveRight()
    self:moveDown()
    self:moveRight()
    self:moveDown()
    self:moveRight()

## 真实姓名
    self:moveRight()
    self:attack("Brak")
    self:attack("Brak")
    self:moveRight()
    self:moveRight()
    self:attack("Treg")
    self:attack("Treg")
    self:moveRight()

## 高举之剑
    self:attack("Rig")
    self:attack("Rig")
    self:attack("Gurt")
    self:attack("Gurt")
    self:attack("Ack")
    self:attack("Ack")

## KITH族的迷宫
    -- 这是一个很长的迷宫…
    self:moveRight()
    self:moveRight()
    self:moveUp()
    self:moveUp()
    
    -- 现在你必须重复以上步骤，再多走一步，走到迷宫的尽头…
    self:moveRight()
    self:moveRight()
    self:moveUp()
    self:moveUp()
    self:moveRight()
    self:moveRight()
    self:moveUp()
    self:moveUp()

## 闹鬼迷宫
    -- loop 让你更容易地反复做事。
    
    loop
    	-- 在这里添加命令来重复。
    	self:moveRight()
    	self:moveRight()
    	self:moveUp()
    	self:moveUp()
    end
    

## 再次迷宫历险
    -- 使用loop循环穿越迷宫！
    loop
    	self:moveRight()
     	self:moveUp()
       	self:moveRight()
       	self:moveDown()
    end

## 恐惧之门
    -- 攻击大门(Door)
    -- 需要攻击很多次,请使用loop循环
    loop
    	self:attack("Door")
    end

## 了解敌人
    -- 你可以用名称标签作为变量。
    
    local enemy1 = "Kratt"
    local enemy2 = "Gert"
    local enemy3 = "Ursa"
    
    self:attack(enemy1)
    self:attack(enemy1)
    
    self:attack(enemy2)
    self:attack(enemy2)
    self:attack(enemy3)
    self:attack(enemy3)

## 名字大师
    -- 你的英雄不知道这些敌人的名字！
    -- 这眼镜给了你寻找最近敌人的能力。
    
    local enemy1 = self:findNearestEnemy()
    self:attack(enemy1)
    self:attack(enemy1)
    
    local enemy2 = self:findNearestEnemy()
    self:attack(enemy2)
    self:attack(enemy2)
    
    local enemy3= self:findNearestEnemy()
    self:attack(enemy3)
    self:attack(enemy3)

## 卑微的KITHMEN
    -- 创建第二个变量并攻击它.
    
    local enemy1 = self:findNearestEnemy()
    self:attack(enemy1)
    self:attack(enemy1)
    local enemy2 = self:findNearestEnemy()
    self:attack(enemy2)
    self:attack(enemy2)
    self:moveDown()
    self:moveRight()
    self:moveRight()
    self:moveRight()

## 近战
    self:moveRight()
    
    -- 通过上一个关卡，你应该能认识这个。
    local enemy1 = self:findNearestEnemy()
    -- 现在，攻击那个变量，
    self:attack(enemy1)
    self:attack(enemy1)
    self:moveRight()
    self:moveRight()
    local enemy2 = self:findNearestEnemy()
    
    
    self:attack(enemy2)
    self:attack(enemy2)
    self:moveRight()
    self:moveRight()

## A MAYHEM OF MUNCHKINS
    -- Inside a loop, use findNearestEnemy and attack!
    
    loop
    	local enemy = self:findNearestEnemy()
    	self:attack(enemy)
    	self:attack(enemy)
    end

## 最后的KITHMAN族
    -- 使用loop循环移动并攻击目标
    loop
    	self:moveRight()
       	self:moveUp()
       	self:moveRight()
       	local enemy=self:findNearestEnemy()
       	self:attack(enemy)
       	self:attack(enemy)
       	self:moveDown()
       	self:moveDown()
       	self:moveUp()
    end

## kithgard之门
    -- 建造三个栅栏来隔离兽人！
    
    self:moveDown()
    self:buildXY("fence", 36, 34)
    self:buildXY("fence", 36, 29)
    self:buildXY("fence", 36, 25)
    self:moveRight()
    self:moveRight()
    self:moveRight()
    self:moveRight()

## kithgard斗殴（特殊关卡）
    -- 在一波波的食人魔攻击中活下来。
    -- 如果你赢了，本关会变得更难，但给更多的奖励。
    -- 如果你输了，你必须等一天之后才能重新提交。
    -- 每次提交都会获得新的随机种子。
    loop
    	local enemy = self:findNearestEnemy()
    	local item = self:findNearestItem()
    	if item then
    		local pos = item.pos
    		self:moveXY(pos.x,pos.y)
     	end 
    	if enemy then
    		if self:isReady("cleave") then
    			self:cleave(enemy)
    		else
    			self:attack(enemy)
    		end
    	else
    		self:shield()
    	end
    end

## kithgard精通（特殊关卡）
    -- 使用移动命令到达迷宫的终点。
    -- 计算你收集到的宝石数量，然后在到达火球陷阱时通过说出当前的宝石数量来使陷阱失效。
    -- 在起点的地方会有一只乌鸦告诉你一个密码。在门的附近说出该密码来开门。
    -- 当你靠近食人魔时杀死它。
    -- 你可以在需要的时候使用loop来重复所有的指令。
    -- 如果你通过了这个关卡，你就可以直接跳到边远地区的森林！
    self:moveUp()
    self:moveRight()
    self:moveRight()
    self:moveRight()
    self:moveUp()
    self:moveDown()
    self:moveRight()
    self:moveRight()
    self:say("Sesame")
    self:moveRight()
    self:moveUp()
    self:say("1")
    self:moveUp()
    self:moveUp()
    enemy = self:findNearestEnemy()
    if enemy then
    	self:attack(enemy)
    	self:attack(enemy)
    end
    self:moveLeft()
    self:moveLeft()
    self:moveLeft()
    self:moveLeft()
    self:moveUp()
    self:moveUp()
    self:moveUp()
    self:moveRight()
    self:moveRight()
    self:moveRight()
    self:moveUp()
    self:moveDown()
    self:moveRight()
    self:moveRight()
    self:say("Sesame")
    self:moveRight()
    self:moveUp()
    self:say("2")
    self:moveUp()
    self:moveUp()
    enemy = self:findNearestEnemy()
    if enemy then
    	self:attack(enemy)
    	self:attack(enemy)
    end
    self:moveLeft()
    self:moveLeft()
    self:moveLeft()
    self:moveLeft()
    self:moveLeft()

## 洞穴求生（特殊关卡）
    -- 生存时间比敌人的英雄长！
    -- 制定自己的战略。有创意!
    loop
    	local   enemy = self:findNearestEnemy()
    	if enemy then
    		if self:isReady("cleave") then
    			self:cleave(enemy)
    		else
    			self:attack(enemy)
    		end
    	else
    		self:shield()
    	end
    end
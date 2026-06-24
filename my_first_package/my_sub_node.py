import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32 # لازم نستخدم نفس نوع الرسالة اللي بعتناها

class DistanceSubscriber(Node):
    def __init__(self):
        super().__init__('distance_subscriber_node')
        
        # إنشاء الـ Subscriber: بيسمع لتوبيك sonar_distance ونوع الرسالة Int32
        # وكل ما رسالة تيجي، بيروح أوتوماتيك ينفذ دالة listener_callback
        self.subscription = self.create_subscription(
            Int32,
            'sonar_distance',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        distance_val = msg.data
        
        # اتخاذ القرار بناءً على قراءة الحساس الحقيقية
        if distance_val < 15:
            self.get_logger().warn('WARNING: Object too close! Distance: %d cm' % distance_val)
        else:
            self.get_logger().info('Safe Zone. Distance: %d cm' % distance_val)

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()

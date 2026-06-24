import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial  # المكتبة الجديدة اللي سيعتمد عليها البرنامج لقراءة الـ USB

class RealSensorPublisher(Node):
    def __init__(self):
        super().__init__('real_distance_publisher_node')
        self.publisher_ = self.create_publisher(Int32, 'sonar_distance', 10)
        
        # فتح اتصال السيريال مع الـ ESP32 بنفس الـ Baud Rate (115200)
        # لو البورت عندك ACM0 غير USB0 لـ ACM0
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
            self.get_logger().info('Serial port /dev/ttyUSB0 opened successfully!')
        except Exception as e:
            self.get_logger().error('Failed to open serial port: %s' % str(e))
            self.get_logger().error('Please check your USB connection or permissions.')

        # التايمر هيشتغل كل 0.1 ثانية (100 ملي ثانية) عشان يواكب سرعة الـ ESP
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        # التأكد من أن البورت مفتوح وهناك بيانات بانتظار القراءة
        if hasattr(self, 'ser') and self.ser.is_open:
            if self.ser.in_waiting > 0:
                try:
                    # قراءة السطر القادم من الـ ESP وفك التشفير وحذف المسافات
                    line = self.ser.readline().decode('utf-8').rstrip()
                    
                    # التأكد أن البيانات المقروءة عبارة عن رقم صحيح فقط
                    if line.isdigit():
                        distance_val = int(line)
                        
                        # تجهيز رسالة الـ ROS وبثها
                        msg = Int32()
                        msg.data = distance_val
                        self.publisher_.publish(msg)
                        self.get_logger().info('Publishing Real Distance: %d cm' % msg.data)
                except Exception as e:
                    self.get_logger().warn('Read error: %s' % str(e))

def main(args=None):
    rclpy.init(args=args)
    node = RealSensorPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if hasattr(node, 'ser') and node.ser.is_open:
            node.ser.close() # إغلاق البورت بأمان عند إيقاف البرنامج
        rclpy.shutdown()

if __name__ == '__main__':
    main()
